import unittest

from code_runner import CodeRunner


code_valid_output = """
def f(x):
    x = x + 1
    return x

print 'This is my output.', f(5)
"""

code_std_error = """
import sys
print "i am gonna give error"
sys.stderr.write('Error! Come on!')
"""
code_compile_error = """
   b=5
"""

code_name_error = """
b=5
grrr
"""

code_infinite_loop = """
while True:
    print("In an infite loop!")
"""


class CodeRunnerTest(unittest.TestCase):
    def test_execute_valid_code(self):
        runner = CodeRunner()

        err, out = runner.run(code_valid_output)
        self.assertEqual(err, '')
        self.assertEqual(out, "This is my output. 6\n")

    def test_execute_code_producing_std_error(self):
        runner = CodeRunner()

        err, out = runner.run(code_std_error)

        self.assertEqual(out, "i am gonna give error\n")
        self.assertEqual(err, 'Error! Come on!')

    def test_execute_code_with_compile_error(self):

        runner = CodeRunner()
        err, out = runner.run(code_compile_error)
        self.assertEqual(out, "")
        self.assertEqual(err, """  File "main.py", line 2\r
    b=5\r
    ^\r
IndentationError: unexpected indent\r
""")

    def test_execute_code_with_name_error(self):

        runner = CodeRunner()
        err, out = runner.run(code_name_error)
        self.assertEqual(out, "")
        self.assertEqual(err, """Traceback (most recent call last):\r
  File "main.py", line 3, in <module>\r
    grrr\r
NameError: name \'grrr\' is not defined\r
""")


    def test_execute_infinite_loop(self):
        runner = CodeRunner()
        err, out = runner.run(code_infinite_loop)

        self.assertEqual(out ,"")
        self.assertEqual(err, "timeout")



