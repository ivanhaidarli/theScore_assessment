Hello everyone

I decided to create only one test case, because all steps mentioned in the requirement doc are not sufficient enough to be a separate test case. Happy to hear points why every step should be a separate test case. Later if more requirements provided, it can be expanded to test suit later.

We have 5 steps that a covered in test.py file and mostly covering navigational functionality of the app. The script verifying that navigation to a certain screen was performant correctly and assure that the right screen is displayed. 

My test script includes:
1. Going with the flow provided in the assessment requirements -> Choosing team or player.
2. Apply Assertions on each step to verify that we are on the same page and elements are visible. If not -> Provided the failed statements to display.
3. Defined timeout as 30 secs and used explicit wait to wait for elements instead of implicit wait.
4. Used implicit wait at one place as app was slow and taking some time to provide results of our query for finding team i-e Toronto Raptors.
5. At the last step I have performed navigation go back to previous screen and put assertions on the previous screen to be sure that we are exactly on the previous screen.

Please let me know if any improvements needed.
FYI, Maven and Gradle is not being provided in my project as I have not used kotlin with my project. I have used python as my own choice, as mentioned in a requirement doc.
Thanks.