Feature: check if a number is even

Scenario Outline: Determine even or odd
Given the number is <number>
When I check if the number is even
Then the result should be "<result>"

Examples:
| number | result  |
| 2      | even    |
| 3      | odd     |
| 4      | even    |
| 5      | odd     |
| 6      | even    |
| 7      | odd     |