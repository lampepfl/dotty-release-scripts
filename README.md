This repository contains scripts for automated Dotty release.

Scripts:

- `checklist.sh` – generates a checklist one must follow to complete the release. Usage: `./checklist.sh <stable_version>`, where `<stable_version>` is the number of the __stable__ version being released.
- `release.sh` – releases the Dotty binaries. Usage: `cd` to the Dotty repo, run the script `release.sh <stable_version>`.
- `ecosystem.sh` – updates the ecosystem projects with the new version of Dotty. Usage: from an empty directory, run the script `ecosystem.sh <stable_version> <live>`. If `<live>` is left out, a dry run will be performed without actually pushing stuff to github. You can set `<live>` to whatever value to perform an actual run.