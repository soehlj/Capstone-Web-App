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
Explain how to file issues, required templates/labels, estimation, and
triage/assignment practices.
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
State how to report vulnerabilities, prohibited patterns (hard-coded secrets),
dependency update policy, and scanning tools.
## Documentation Expectations
Specify what must be updated (README, docs/, API refs, CHANGELOG) and
docstring/comment standards.
## Release Process
Describe versioning scheme, tagging, changelog generation, packaging/publishing
steps, and rollback process.
## Support & Contact
Provide maintainer contact channel, expected response windows, and where to ask
questions.
