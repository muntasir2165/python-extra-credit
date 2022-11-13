# Python Extra Credit

## Python Mitigation

Python mitigation is the technique and methodology of using Python to mitigate against potential security vulnerabilities.

One example of a security vulnerability in the domain of the Python programming language involves the `eval()` function. Unless handled correctly, the use of this function could lead to execution of code injection attacks via malicious user inputs. One possible way to mitigate again this kind of attack would be to search for characters or patterns in the user input that we expect the input to be for the required evaluation. If the input deviates from the expected pattern, we can reject the input and stop any further processing until the correct input is provided. Alternatively, we could sanitize the user input by scrubbing the non-matching characters/patterns as needed, thus rendering the attack ineffective.

## Getting Help

If help is needed to understand something in the repo or just to provide feedback/suggestion, please send an email to muntasir2165@hotmail.com

## Author

**Muntasir Biojid** - [GitHub Profile](https://github.com/muntasir2165)
