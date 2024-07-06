def validate_inputs(question: str = "", validate=None) -> str:
  '''This is an old function that checks if the type an string is, you can make it better if you have better ideas'''
  supplied = input(question)
  if validate is None:
      return supplied
  else:
      return validate(supplied)
