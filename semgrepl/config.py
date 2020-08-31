import os
import logging
from typing import List, Dict
import semgrepl.tokei as tokei

# TODO: should infer this from semgrep somehow
SEMGREP_SUPPORTED_LANGUAGES = ["python", "go", "java", "javascript", "ruby"]

class SemgreplConfig:
    """ Object holding configuration for targets.
    """
    def __init__(self, targets, rules_dir = "", default_language = None):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.rules_dir = os.path.abspath(rules_dir)
        self.default_language = default_language

        self.targets = targets

        # Make all targets absolute paths
        self.targets = [os.path.abspath(x) for x in targets]

        # Maps repo root to languages used
        self.languages_used = {}

        # Run tokei on all targets
        logging.info("Determining languages used in target repos...")
        for target in self.targets:
            # for ease of reference, just have the base dirname of the repo
            # be the key
            key = os.path.basename(target)
            self.languages_used[key] = tokei.Tokei.run(target)
        logging.info("Finished language detection.")

        # self.languages is the union list of languages used in any repo
        # in [targets] that semgrep can currently parse
        self.languages = self.semgrep_supported_langs_any_repo(self.languages_used)

        self.print_languages_used()


    def print_languages_used(self):
        for repo, tokei_output in self.languages_used.items():
            logging.info("{}".format(repo))
            tokei_output.print_languages_used()
            print()

    def __repr__(self):
        return "<SemgreplConfig rules_dir={}, default_language={}, targets={}, languages_used={}".format(
            self.rules_dir, self.default_language, self.targets,
            self.languages_used)

    def semgrep_supported_langs_any_repo(self, langs: Dict[str, tokei.TokeiOutput]):
        result = set()
        for repo, tokei_output in langs.items():

            for lang in tokei_output.language_names:
                if lang.lower() in SEMGREP_SUPPORTED_LANGUAGES:
                    result.add(lang.lower())

        return list(result)
