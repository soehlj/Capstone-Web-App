# Contributing Guide
How to set up, code, test, review, and release so contributions meet our Definition
of Done.
## Code of Conduct
It is expected that all contributions are kept professional and on focus, and no malicious commits should be created in any way.
## Getting Started
There are currently no prerequisites for this program. In it's current state the index.html page can be loaded in your browser as a file.
## Branching & Workflow
We will be using a more git-flow type system. Every feature that is implemented
will be first implemented on it's own branch and once it acheives it's definition
of done, it can be merged with the main branch.

The naming of branches should be as concise as possible and clearly understandable.
example: Models Page, Embed Content on Page
## Issues & Planning
Issues should be filed through the github issues feature as well as a message in the team discord outlining the problem.
## Commit Messages
With each commit, the message should be concise but give details about what was changed.
The specific lines of code generally won't need mentioned, but the functionality that changed or
was added should be noted in the commit message.
examples:
"fixed error with main page"
"added embedded content to page"
"removed unused code"
## Code Style, Linting & Formatting
Config files are in .prettierrc and .eslintrc.json. Run npm run lint to check and npm run lint:fix or npm run format to fix issues. Code must pass linting before merge.
## Testing
All code changes must include tests. Run tests with npm test. Unit and integration tests are required for new features or bug fixes. Test coverage should stay above 80%.
when new/updated tests are mandatory.
## Pull Requests & Reviews
Use the pull request template and link related issues. All PRs must pass lint, tests, and CI checks before review. At least one reviewer must approve before merge. Keep PRs small and focused.
## CI/CD
CI/CD is handled through GitHub Actions in .github/workflows/. Jobs include lint, test, and build. All jobs must pass before merging or releasing. Logs and reruns are available under the Actions tab.
## Security & Secrets
Vulnerabilities, prohibited patterns (hard-coded secrets),dependency update policy, and scanning tools can all be reported through github issues or by emailing any team member.
## Documentation Expectations
All code must be thoroughly commentedto describe its purpose. 
Upon adding any dependecies to the project or large refrences the README must also be update to describe the new scope.
## Release Process
This project follows a lightweight release workflow to ensure stable, trackable versions.
Versioning Scheme
Uses Semantic Versioning (SemVer): MAJOR.MINOR.PATCH
MAJOR — breaking changes
MINOR — new features, backward-compatible
PATCH — bug fixes and small improvements
Pre-release suffixes may be used: -alpha, -beta, -rc

Changelog entries are maintained in CHANGELOG.md

Packaging / Publishing - 
Go to Releases → Draft new release
Select tag or create one
Paste changelog entry
Upload artifacts (if applicable)
Publish

Rollback Process
If a release is bad:
Tag rollback
Revert merge/commit
Push a patched version (e.g., vX.Y.Z+1, vX.Y.Z-1, or vX.Y.(Z+1))
Mark previous release as deprecated in the GitHub release notes
## Support & Contact
All Team Members can be contacted throughthe github issues function, there is an expected response window of 3-4 days.
