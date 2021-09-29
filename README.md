# Develop with the Perspective of the Tester in mind
[![build status of master](https://travis-ci.org/jjzcru/GitHubApi567.svg?branch=main)](https://travis-ci.org/jjzcru/GitHubApi567)

## Author
Jose J. Cruz

## Description

### Background

This assignment will require that you write code to interface with an external REST-based APIs.   We could have used almost any external APIs, but for this assignment we chose GitHub because many of its APIs are public and do not require any authorization or API Keys.   This simplifies both the use and setup.


For this assignment imagine that you have been asked to develop a function that will interface with GitHub in order to extract and present useful information to your user. The function will communicate using the RESTful services APIs provided by GitHub. The GitHub APIs will allow you to query for information about users, repositories, etc... which can be retrieved using the function, and then be displayed in the application.

What should make this assignment different from other programming assignments is in how you will approach it.  You should approach this assignment as a developer who more than anything else has the perspective of the tester in the front of your mind. 

The developer looks at the requirements and asks how should I design and implement this function, but the tester will ask questions such as what will I need to test for in this function?  And how will I test this function?   As you design and write the function as a developer, you should consider the perspective of the tester in any of your design and implementation decisions.   One deliverable of this assignment will be to reflect and comment on this.

Note:  we will be building on this assignment for next week, so you will definitely need to complete this assignment this week.

### Requirements

You should write a function that will take as input a GitHub user ID. 
The output from the function will be a list of the names of the repositories that the user has, along with the number of commits that are in each of the listed repositories.


So, for example, if user John567 has 2 repositories named "Triangle567" and "Square567" each with some number of commits, then the function might output :

```
Repo: Triangle567 Number of commits: 10
Repo: Square567 Number of commits: 27
```

### Important
The purpose of this assignment is NOT about writing a complex or pretty function.  This should be a simple implementation, and in fact, the implementation is small relative to the Triangle programming assignment.  But think about how you will test the function and how you can make testing easy to implement. 
Design and write the program in a way that will make it easy for anyone to test.

In addition to the function you should also include some unit tests similar to how you tested the Triangle program in HW 02a to prove to yourself that the program is behaving correctly.