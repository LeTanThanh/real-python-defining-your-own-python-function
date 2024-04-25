if __name__ == "__main__":
  # Functions in Python

  s = "foobar"
  print(s)
  print(id(s))

  a = ["foo", "bar", "baz", "qux"]
  print(a)
  print(len(a))

  print(any([False, False, False]))
  print(any([False, True, False]))

  print(any(["bar" == "baz", len("foo") == 4, "qux" in {"foo", "bar", "baz"}]))
  print(any(["bar" == "baz", len("foo") == 3, "qux" in {"foo", "bar", "baz"}]))

  # The Importance of Python Functions
  ## Abstraction and Reusability
  ## Modularity
  ## Namespace Separation

  # Function Calls and Definition

  """
  def <functionname>([<parameters>]):
    <statement(s)>
  """

  # def f():
  #   s = "-- Inside f()"
  #   print(s)

  # print("Before calling f()")
  # f()
  # print("After calling f()")

  # Argument Passing
  ## Positional Arguments

  # def f(qty, item, price):
  #   print(f"{qty} {item} cost ${price:.2f}")

  # f(6, "banana", 17.4)

  ## Keyword Arguments

  # f(qty = 6, item = "banana", price = 17.4)

  ## Default Parameters

  # def f(qty = 6, item = "bananas", price = 1.74):
  #   print(f"{qty} {item} cost ${price:.2f}")

  # f(4, "apples", 2.24)
  # f(4, "apples")
  # f(4)
  # f()
  # f(item = "kumquats", qty = 9)
  # f(price = 2.29)

  ## Mutable Default Parameter Values

  """
  Things can get weird if you specify a default parameter value that is a mutable object.
  Consider this Python function define
  """

  # def f(my_list = []) -> list:
  #   my_list.append("###")
  #   return my_list

  """
  f() takes a single list parameter, appends the string "###" to the end of the list, and returns the result:
  """

  # print(f(["foo", "bar", "baz"])) # ["foo", "bar", "baz", "###"]
  # print(f([1, 2, 3, 4, 5])) # [1, 2, 3, 4, 5, "###"]

  """
  The default value for parameter my_list is the empty list, so if f() is called without any arguments, then the return value is a list with the single element "###"
  """

  # print(f()) # ["###"]

  """
  Everything makes sense so far.
  Now, what would you except to happen if f() is called without any parameters a second and a third time? Let's see:
  """

  # print(f()) # ["###", "###"]
  # print(f()) # ["###", "###", "###"]

  """
  Oops! You might have expected each subsequent call to also return the singleton list ["###"], just like the first.
  Instead, the return value keeps growing. What happended?

  In Python, default parameter values are defined only once when the function is defined (that is, when def statement is executed).
  The default value isn't re-defined each time the function is called.
  Thus, each time you call f() without a parameter, you're performing .append() on the same list.

  You can demonstrate this with id():
  """

  # def f(my_list = []) -> list:
  #   print(id(my_list))
  #   my_list.append("###")
  #   return my_list

  # print(f())
  # print(f())
  # print(f())

  """
  The object identifier displayed confirms that, when my_list is allowed to default, the value is the same object with each call.
  Since lists are mutable, each subsequent .append() call to causes the list to get longer.
  This is a common and pretty well-documented pitfall when you're using a mutable object as a parameter's default value.
  It potentially leads to confusing code behavior, and is probably best avoided.

  As a wordaround, consider using a default argument value that signals no argument has been specified.
  Most any value would work, but None is a common choice.
  When the sentinel value indicates no argument is given, create a new empty list inside the function:
  """

  def f(my_list = None) -> list:
    if my_list is None:
      my_list = []

    my_list.append("###")
    return my_list

  print(f())  # ["###"]
  print(f())  # ["###"]
  print(f())  # ["###"]
  print(f(["foo", "bar", "baz"])) # ["foo", "bar", "baz", "###"]
  print(f([1, 2, 3, 4, 5]))       # [1, 2, 3, 4, 5, "###"]

  """
  Note how this ensures that my_list now truthy defaults to an empty list whether f() is called without an argument.
  """

  ## Pass-By-Value vs Pass-By-Reference in Pascal
  ## Pass-By-Value vs Pass-By-Reference in Python
  ## Argument Passing Summary
  ## Side Effects

  # The return Statement
  ## Exiting a Function
  ## Returning Data to the Caller
  ## Revisiting Side Effects

  # Variable-Length Argument Lists
  ## Argument Tuple Packing
  ## Argument Tuple Unpacking
  ## Argument Dictionary Packing
  ## Argument Dictionary Unpacking
  ## Putting It All Together
  ## Multiple Unpackings in a Python Function Call

  # Keyword-Only Arguments

  # Positional-Only Arguments

  # Docstrings

  # Python Function Annotations
