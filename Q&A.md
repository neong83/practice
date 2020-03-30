# Question & Answer

<br/><br/>
##  **Gherkin Questions**
> Why Gherkin tests in `tests/features/sort_strings_in_descending_alphabet_order.feature` might be helpful in future?

One of the best features from Gherkin is the ability to directly convert user stories into executable tests.  They are readable to both developers and project managers.  

These readability allow project managers to use it as reference to capture features which is currently supporting, provide a flexible way for developers to communicate edge cases with them, and setup tests before the ticket has started. 

Overall, it makes sure continuous integration will preserve the existing features, developers can implement features with predefined validations, project managers can write tests to verify ideas / capabilities before the ticket ever gets created, and allows new developers to understand applications easily.

For example, readers can fully understand this project will only accept English words from CSV, sort them in descending alphabetical order,  and write out to another CSV file within 30 seconds after taking a look at `sort_strings_in_descending_alphabet_order.feature`.  

Thus, having Gherkin tests in a project is really useful.

<br/><br/>
## **Tool questions**
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

<br/><br/>
> What are some pros and cons of using Docker to develop, test, and deploy software?

Pros:
- It’s light-weight
- It allows developer to create base image with all the 3rd library, configurations, etc for application to run on
- It allows developer only need to set it up once and it can be share with others
- It allows developer to quickly rollback (rebuild image) when their changes had broken the container
- It makes switching / deploy to another environment easy
- Developer does not have to worry about unexpected behavior due to environment changes (ie. from Dev to Stage, or works on my machine situation)
- New deployment will only takes seconds to start up
- Each container can force on only one subject that matters
- Developer can create cluster to allow contains work together

Cons:
- You need to know what you are doing
- It’s does not persist data
- Docker is target for server applications
- You need to build container to read in secret rather than create image with embedded secret

<br/><br/>
> How do you choose which language to use for a given task? How did you choose the language for the programming exercise above?

I will determine the language basis on requirements, running platform, language adoption rate, and if it is an existing project within the company.  As switching from one language to another requires total rewriting, it takes time and investment for the company to move it over.  Thus, there are not too many options to choose what language to use for a given task.  It usually requires the developer to quickly learn the new language and start providing business value as a result.

And the reason I had chosen Python as my programming language is because:
- This is a new project
- Python is the language the team is using for this position I am applying
- Python can written as small script to handle business needs
- Python provide lots flexibility to write codes (single responsibility, object oriented design, etc)
- The requirement was asking to build an application runnable with Docker command
- I know Python better than other languages 


<br/><br/>
## **Testing Methodology questions**

> When is it appropriate to use automated testing? 

- Manually repeat tests take time
- Avoid human error during repeat tests
- Provide fast result
- Make sure PR is stable before code review
- And validation application persist expected behaviors

<br/><br/>
> When is it appropriate to use manual testing?

- Validate new implementation fits business requirement
- Uncover edge cases
- Make sure implementation works well with other part of system (ie. front end)
- And a good way to validate PR

<br/><br/>
> What factors do you think about as you decide where to focus testing efforts? 

I am a big fan of testing, I believe having too many tests is better than not having enough tests.  I like to set up unit and integration tests from individual methods, method interactions, and all the way to workflow.   It can provide me the confidence to ensure the application does what intended.

In addition, I also like to provide unit tests to bugs that were discovered / fixed, so users won’t have to face the same problems again in future.    

<br/><br/>
> How do you decide what not to test?

- Class with no implementation (like abstract base class) 
- Helper methods uses inside testing
- 3rd party libraries (except the behavior application is currently using)
- Configurations 
- Standard libraries
