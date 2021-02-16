This repository contains scripts for automated Dotty release.

Scripts:

- `checklist.sh` – generates a checklist one must follow to complete the release. Usage: `./checklist.sh <stable_version>`, where `<stable_version>` is the number of the __stable__ version being released.
- `release.sh` – releases the Dotty binaries. Usage: `cd` to the Dotty repo, run the script `release.sh <stable_version>`.
- `ecosystem.sh` – updates the ecosystem projects with the new version of Dotty. Usage: from an empty directory, run the script `ecosystem.sh <stable_version> <live>`. If `<live>` is left out, a dry run will be performed without actually pushing stuff to github. You can set `<live>` to whatever value to perform an actual run.

# Ecosystem Release Usage
1. In the file `release_version`, specify the version of Dotty being released
2. The `./ecosystem <project_name>` command will check out the given project, modify it appropriately, test it, and, if the tests are successful, will push the changes to upstream or submit a PR depending on the project's settings.