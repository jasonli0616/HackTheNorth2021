# Hack The North 2021

This repo is for our [Hack The North](https://hackthenorth.com) project.

From our [Devpost submssion](https://devpost.com/software/budget-calculator-sv6iyf):

### What Inspired Us

There are many budgeting apps out there, but not very many allow you to visualize the impact your everyday purchases are having on your bank account. This inspired us to create an app to solve this exact problem as Budget Visualizer is a user-friendly website that displays your budget in the form of a chart.

### What We Learned

In the creation of Budget Visualizer, we learned how to use MongoDB to store the user's information including their email, username, password, and budget items. Furthermore, we learned how to use Chart.js, a Javascript library that allowed us to visually display the user's budgeting information.

### How We Built It

We used a Python backend for the website. Using the Flask framework, we were able to create a modular and powerful backend. The Python code directly updates the MongoDB database, which stores user information and budget information. The user is able to create and edit their information using the frontend of our website, which is built using HTML, JavaScript, and Bootstrap.

### Challenges We Faced

One of our challenges, the delete button functionality, was hard to nail down. It was difficult to make sure the item input was being deleted. However, we solved it by using a for loop to give items a specific id and then sent that id to the delete_item() function when the button was clicked to know the exact item to delete.