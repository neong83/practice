# Question & Answer

###  **Gherkin Questions**
#### _Why Gherkin tests in `tests/features/sort_strings_in_descending_alphabet_order.feature` might be helpful in future?_

One of the best features from Gherkin is the ability to directly convert user stories into executable tests.  They are readable to both developers and project managers.  

These readability allow project managers to use it as reference to capture features which is currently supporting, provide a flexible way for developers to communicate edge cases, and setup tests before the ticket has started. 

Overall, it makes sure continuous integration will preserve the existen features, developers can implement features with predefined validations, project managers can write tests to verify ideas / capabilities before the ticket ever gets created, and allows new developers to understand applications easily.

For example, readers can fully understand this project will only accept English words from CSV, sort them in descending alphabetical order,  and write out to another CSV file within 30 seconds after taking a look at `sort_strings_in_descending_alphabet_order.feature`.  

Thus, having Gherkin tests in a project is really useful.
