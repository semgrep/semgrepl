from typing import List
from io import StringIO
from semgrep.output import OutputHandler
from semgrep.output import OutputSettings
from semgrep.constants import OutputFormat
from collections import defaultdict
import semgrep.semgrep_main
import json
import os

def semgrep_pattern(pattern: str, targets: List[str], config = ""):
    io_capture = StringIO()
    output_handler = OutputHandler(
        OutputSettings(
            output_format=OutputFormat.JSON,
            output_destination=None,
            error_on_findings=False,
            strict=False,
        ),
        stdout=io_capture,
    )
    semgrep.semgrep_main.main(
        output_handler=output_handler,
        target=[str(t) for t in targets],
        pattern=pattern,
        config=config,
        lang="python")
    output_handler.close()
    return json.loads(io_capture.getvalue())

class SemgreplObject:
    pass

class SemgreplImport(SemgreplObject):
    def __init__(self, match):
        metavars = match['extra']['metavars']
        self.file_path = match['path']

        if '$X' in metavars:
            self.import_path = metavars['$X']['abstract_content']
            self.md5sum = metavars['$X']['unique_id']['md5sum']
        else:
            print("Failed on file: " + self.file_path)
            self.import_path = "FAILED"

    def __repr__(self):
        return "<SemgrepImport file_path={} import_path={}>".format(self.file_path, self.import_path)

    def __hash__(self):
        return hash(self.import_path + self.file_path)

    def __eq__(self, other):
        return self.file_path == other.file_path and self.import_path == other.import_path



def collect_matches(fn, matches : List[SemgreplObject]):
    ret = defaultdict(set)
    for match in matches:
        k = fn(match)
        ret[k].add(match)

    return ret

# Organize SemgreplImports
def collect_imports(imports : List[SemgreplImport]):
    return collect_matches(lambda i: i.import_path, imports)

# Dict returned from collect_matches: {"string_key": [SemgreplObj1, ...]}
# Returns: {"key": count, "key2": count}
def count_collection(obj_collection):
    result = {}
    for key, items in obj_collection.items():
        result[key] = len(items)
    return result

def find_imports(target, rules_dir) -> List[SemgreplImport]:
    # TODO: generalize across other langs
    python_import_rule_path = os.path.join(rules_dir, "python", "python-imports.yaml")
    matches = semgrep_pattern("", [target], python_import_rule_path)

    import_matches = [SemgreplImport(x) for x in matches['results']]    
    matches = collect_imports(import_matches)
    counts = count_collection(matches)
    import ipdb; ipdb.set_trace()
    return matches
