"""
Sample String: "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are!"

- The print() function doesn’t support the “softspace” feature of the old print statement. For example, in Python 2.x, print "A\n", "B" would write "A\nB\n"; but in Python 3.0, print("A\n", "B") writes "A\n B\n".
- Initially, you’ll be finding yourself typing the old print x a lot in interactive mode. Time to retrain your fingers to type print(x) instead!
- When using the 2to3 source-to-source conversion tool, all print statements are automatically converted to print() function calls, so this is mostly a non-issue for larger projects.
"""

txt = "Twinkle, twinkle, little star,\n\t How I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are"
print(txt)
