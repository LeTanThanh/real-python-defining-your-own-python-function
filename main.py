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

  def f(qty, item, price):
    print(f"{qty} {item} cost ${price:.2f}")

  f(6, "banana", 17.4)

  ## Keyword Arguments

  f(qty = 6, item = "banana", price = 17.4)

  ## Default Parameters
  ## Mutable Default Parameter Values
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
