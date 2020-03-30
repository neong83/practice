# Question & Answer

###  **Gherkin Questions**
> Why Gherkin tests in `tests/features/sort_strings_in_descending_alphabet_order.feature` might be helpful in future?

One of the best features from Gherkin is the ability to directly convert user stories into executable tests.  They are readable to both developers and project managers.  

These readability allow project managers to use it as reference to capture features which is currently supporting, provide a flexible way for developers to communicate edge cases with them, and setup tests before the ticket has started. 

Overall, it makes sure continuous integration will preserve the existing features, developers can implement features with predefined validations, project managers can write tests to verify ideas / capabilities before the ticket ever gets created, and allows new developers to understand applications easily.

For example, readers can fully understand this project will only accept English words from CSV, sort them in descending alphabetical order,  and write out to another CSV file within 30 seconds after taking a look at `sort_strings_in_descending_alphabet_order.feature`.  

Thus, having Gherkin tests in a project is really useful.


### **Tool questions**
> In your opinion, what’s helpful about version control systems? What’s annoying about them?

Pros:
- It makes rollback on production easy
- It allows developers quickly rollback when entered bad state (ie. refactor)
- It allows developers work on features (branches) independently (ie. continuous integration)
- It allows content switch easy
- It allows project to reference 3rd party library with specific version and won’t have to worry about unexpected behaviors on new releases
- It allows developer to cherry pick commits from other unmerged branches
- It allows automated testing and easy deployment
- It provides branch restrictions
- It provides a history of changes / improvement made overtime
- It provides easy code review
- It provides developer a way to find the last person edit / develop the code when there are questions

Cons:
- Another commit is required when small mistake was made from last commit
- Reverse a commit taken another commit
- Each branch has a force on what need to be done (cannot outside of scope)
- A new JIRA ticket is required when unrelated (to current branch) bug is found
- It will become a disaster if developer does not familiar with GitHub flow
- Commits are not allow to remove from upstream, unless remove remote branch (must be super careful)
