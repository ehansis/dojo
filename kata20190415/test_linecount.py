from . import linecount


test_1 = """// This file contains 3 lines of code
public interface Dave {
  /**
   * count the number of lines in a file
   */
  int countLines(File inFile); // not the real signature!
}
"""

test_2 = """/*****
* This is a test program with 5 lines of code
*  \/* no nesting allowed!
//*****//***/// Slightly pathological comment ending...

public class Hello {
    public static final void main(String [] args) { // gotta love Java
        // Say hello
      System./*wait*/out./*for*/println/*it*/("Hello/*");
    }

}
"""


class TestCount:

    def test_nc(self):
        assert linecount.code_lines(test_1) == 3
        assert linecount.code_lines(test_2) == 5
