Feature: Sort strings in descending alphabetical order
  Read in all strings from CSV file
  Sort them into descending alphabetical order
  Write output into CSV file

  Scenario: App is able to sort English words in CSV
    Given a "input.csv" file with "Copenhagen,Stockholm,Oslo"
    When read in CSV file
    Then write to "output.csv" file with "Stockholm,Oslo,Copenhagen"

  Scenario: App ignores foreign language in CSV
    Given a "input.csv" file with "它,他,她"
    When read in CSV file
    Then write to "output.csv" file with ""

  Scenario: App ignores symbols in CSV
    Given a "input.csv" file with "*,(,%"
    When read in CSV file
    Then write to "output.csv" file with ""

  Scenario: App ignores numbers in CSV
    Given a "input.csv" file with "1,2,3"
    When read in CSV file
    Then write to "output.csv" file with ""

  Scenario: App ignores letter and number mixed words in CSV
    Given a "input.csv" file with "BY2,B2B,A1A"
    When read in CSV file
    Then write to "output.csv" file with ""

  Scenario: App is able to sort English words with leading and / or trailing spaces in CSV
    Given a "input.csv" file with "   Copenhagen   ,Stockholm   ,   Oslo"
    When read in CSV file
    Then write to "output.csv" file with "Stockholm,Oslo,Copenhagen"
