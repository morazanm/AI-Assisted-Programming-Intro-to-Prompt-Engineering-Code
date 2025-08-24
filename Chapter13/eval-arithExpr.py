

""" 
  An env is an object
    instance variable: bindings is a (listof (String number))
    Interface:
      addBindings: 
        Signature: (listof String) (listof number) -> env
        Purpose: Add bindings corresponding to given list elements
                 to the front of bindings
        Assume: Given lists are of the same length
        Design Idea:
          Simultaneously traverse the given list
          At each step add (current String, current Value) to the front of bindings

      apply:
        Signature: String -> number
        Purpose: Returns the value of the given variable
        Design Idea:
          Use structural recursion on bindings to return the value of the given variable
          if bindings is empty return error stating the given variable is unbound, include the variable name in the error message
          elif if given variable is equal to the string in bindings first pair return the number in bindings first pair
          else recursively process the rest of bindings

  Define a class for environment
"""
class Env:
  def __init__(self, bindings=None):
    if bindings is None:
      bindings = []
    self.bindings = bindings

  def addBindings(self, names, values):
    if len(names) != len(values):
      raise ValueError("Names and values must have the same length")
    new_bindings = list(zip(names, values)) + self.bindings
    return Env(new_bindings)

  def apply(self, var):
    for name, value in self.bindings:
      if name == var:
        return value
    raise ValueError(f"Unbound variable: {var}")


"""
Data Definitions

Concrete Grammar
  E -> numE | appE | varE
  numE -> number
  varE -> str
  appE -> [op loE]
  op -> '+' | '-' | '*' | '/' | funct
  funct -> ['lam' losymb expr]

Abstract Syntax
  An op is an object
    instance variables: op is either:
                          1. '+' 
                          2. '-'
                          3. '*'
                          4. '/'
                          5. lam
    interface:
      getop:
        Signature: -> str or lam
        Purpose: Return the operator
        Design Idea: return op
      unparse:
        Signature: -> str
        Purpose: Convert the operator to its concrete grammar form
        Design Idea:
          if self.op in ['+', '-', '*', '/']:
              return self.op
          else:
              return self.op.unparse()

  A lam is an object
    instance variables: params and body
    Interface:
      getparams:
        Signature: -> (listof str)
        Purpose: Return the parameters
        Design Idea: return params
      getbody:
        Signature: -> expr
        Purpose: Return the body
        Design Idea: return body
      unparse:
         Signature: -> funct
         Purpose: Convert the lam to its concrete grammar form
         Design Idea: return ['lam', params, body.unparse()]
              
  An expr is an object
    instance variable: exp is either 1. numExpr 2. varExpr or 3. a appExpr
    Interface:
      getexp:  
       Signature: -> exp
       Purpose: Return the expression
       Design Idea: return exp
     unparse:
         Signature: -> E
         Purpose: Convert the expression to its concrete grammar form
         Design Idea: return exp.unparse()
     eval:
       Signature: env -> number
       Purpose: Evaluate exp
       Accumulator Invariant: 
         env = (listof bindings) for lexically visible variables
       Design Idea: return exp.eval(env)
  
  A numExpr is an object
    instance variable: num
    Interface:
      getnum:
        Signature: -> number
        Purpose: Return the number
        Design Idea: return num
      unparse:
        Signature: -> number
        Purpose: Convert the number expression to its concrete grammar form
        Design Idea: return num
      eval:
       Signature: env -> number
       Purpose: Evaluate the expression
       Accumulator Invariant: 
        env = (listof bindings) for lexically visible variables
       Design Idea: return num

  A varExpr is an object
    instance variable: var
    Interface:
      getvar:
        Signature: -> str
        Purpose: Return the variable name
        Design Idea: return var
      unparse:
        Signature: -> str
        Purpose: Convert the variable expression to its concrete grammar form
        Design Idea: return var
      eval:
       Signature: env -> number
       Purpose: Return the value of the variable
       Accumulator Invariant: 
         env = (listof bindings) for lexically visible variables
       Design Idea: return env.apply(var)

  An appExpr is an object
    instance variables: operator and args
    Interface:
      getop:
        Signature: -> op
        Purpose: Return the operator
        Design Idea: return operator
      getargs:
        Signature: -> (listof expr)
        Purpose: Return the arguments
        Design Idea: return args
      unparse:
        Signature: -> [op loE]
        Purpose: Convert the application expression to its concrete grammar form
        Design Idea: return a list with the unparsed operator and the unparsed arguments
      eval:
       Signature: env -> number
       Purpose: Evaluate the expression
       Accumulator Invariant: 
         env = (listof bindings) for lexically visible variables
       Design Idea:
         evaluate all the arguments
         Call apply with op args
"""

"""
Define objects for op, lam, expr, numExpr, varExpr, and appExpr
"""
class op:
    def __init__(self, op):
        self.op = op

    def getop(self):
        return self.op
    
    def unparse(self):
        if self.op in ['+', '-', '*', '/']:
            return self.op
        else:
            return self.op.unparse()

class lam:
    def __init__(self, params, body):
        self.params = params
        self.body = body

    def getparams(self):
        return self.params

    def getbody(self):
        return self.body
    
    def unparse(self):
        return ['lam', self.getparams(), self.getbody().unparse()]
    
class expr:
    def __init__(self, exp):
        self.exp = exp

    def getexp(self):
        return self.exp
    
    def eval(self, env):
        return self.exp.eval(env)
    
    def unparse(self):
        return self.exp.unparse()
    
class numExpr:
    def __init__(self, num):
        self.num = num

    def getNum(self):
        return self.num
    def eval(self, env):
        return self.num
    def unparse(self):
        return self.num

class varExpr:
    def __init__(self, var):
        self.var = var

    def getvar(self):
        return self.var
    
    def eval(self, env):
        return env.apply(self.var)
    
    def unparse(self):
        return self.var

class appExpr:
    def __init__(self, operator, args):
        self.operator = operator
        self.args = args

    def getop(self):
        return self.operator

    def getargs(self):
        return self.args
    
    def eval(self, env):
        evaluated_args = [arg.eval(env) for arg in self.args]
        return apply(self.operator, evaluated_args, env)
    
    def unparse(self):
        return [self.operator.unparse()] + [arg.unparse() for arg in self.args]

def apply(operator, args, env):
    """
    Signature: operator (listof number) -> number
    Purpose: Apply the op to the given arguments
    Design idea:
      op is a list: ['lam' params body], where params is a (listof string) and body is an expr
      if op is '+' add all the args
      elif op is '-' subtract all the args
      elif op is '*' multiply all the args
      elif op is '/' divide all the args
      elif if op is a lam eval op's body in a new environment with bindings for op's params and args
      else raise an error stating the operator is invalid, include the operator in the error message
    """
    if isinstance(operator, lam):
        params = operator.getparams()
        body = operator.getbody()
        if len(params) != len(args):
            raise ValueError("Number of parameters and arguments must be the same")
        new_env = env.addBindings(params, args)
        return body.eval(new_env)
    elif isinstance(operator, op):
        prim = operator.getop()
        if prim == '+':
            return sum(args)
        elif prim == '-':
            if len(args) == 0:
                raise ValueError("Subtraction requires at least one argument")
            result = args[0]
            for num in args[1:]:
                result -= num
            return result
        elif prim == '*':
            result = 1
            for num in args:
                result *= num
            return result
        elif prim == '/':
            if len(args) == 0:
                raise ValueError("Division requires at least one argument")
            result = args[0]
            for num in args[1:]:
                if num == 0:
                    raise ValueError("Division by zero is not allowed")
                result /= num
            return result
        else:
            raise ValueError(f"Invalid operator '{prim}'")
    else:
        raise ValueError("Invalid operator type")
    
def test_apply():
    """
    Signature:   -> None
    Purpose: Test apply
    Design Idea:
      env0 = generate an empty environment
      env1 = generate envionment with at least 3 bindings
      lam1 = generate a one-input lam op
      lam3 = generate a three-input lam op
      Test '+', '-', '*', and '/' with env0 and env1
      Test lam1 and lam3 with env1
    """
    env0 = Env([])
    env1 = Env([]).addBindings(['x', 'y', 'z'], [1, 2, 3])
    
    lam1 = lam(['a'], expr(numExpr(10)))
    lam3 = lam(['x', 'y', 'z'], expr(appExpr(op('+'), [varExpr('x'), varExpr('y'), varExpr('z')])))
    
    test_cases = [
        (op('+'), [1, 2, 3], 6),
        (op('-'), [10, 5], 5),
        (op('*'), [2, 3, 4], 24),
        (op('/'), [12, 4, 3], 1.0),
        (lam1, [5], 10),
        (lam3, [1, 2, 3], 6)
    ]
    for operator, args, expected in test_cases:
        result = apply(operator, args, env0 if operator == lam1 else env1)
        assert result == expected, f"Test failed for apply with operator {operator.getop()} and args {args}, expected {expected} but got {result}"

test_apply()

def parseE(an_e):
    """
    Signature: E -> expr throws error
    Purpose: Parse the given concrete grammar expression
    Design Idea:
      Use structural recursion to build an expr form the given concrete grammar expression
      If an_e is a list and an_e[0] is of the form ['lam' params body], return expr(appExpr(parseLambda(an_e[0]), parseArgs(an_e[1:])))
      else return expr(appExpr(op(an_e[0]), parseArgs(an_e[1:])))
    """
    def parseLambda(alam):
      """
      Signature: function -> op
      Purpose: Parse the given lambda
      Design Idea: return lam(alam[1], parseE(alam[2]))
      """
      return lam(alam[1], parseE(alam[2]))

    def parseArgs(loE):
      """
      Signature: (listof E) -> (listof expr)
      Purpose: Parse the given list of concrete expressions
      Design Idea: Traverse and parse each element of the list
      """
      return [parseE(e) for e in loE]

    if isinstance(an_e, list):
        if an_e[0][0] == 'lam':
            return expr(appExpr(parseLambda(an_e[0]), parseArgs(an_e[1:])))
        else:
            return expr(appExpr(op(an_e[0]), parseArgs(an_e[1:])))
    elif isinstance(an_e, (int, float)):
        return expr(numExpr(an_e))
    elif isinstance(an_e, str):
        return expr(varExpr(an_e))
    else:
        raise ValueError("Invalid expression format")
    
def test_parseE():
    """
    Signature:  -> None
    Purpose: test parseE
    Design Idea:
      numexp = generate an E with a numE
      plusexp = generate an E with an appE using a primitive op: '+'
      minusexp = generate an E with an appE using a primitive op: '-'
      multexp = generate an E with an appE using a primitive op: '*'
      divexp = generate an E with an appE using a primitive op: '/'
      lexp1 = generate an E with an appE using a funct op
      lexp2 = generate an E with an appE using a funct op
      for e in [numexp, plusexp, minusexp, multexp, divexp, lexp1, lexp2]:
        assert e.unparse() == expected expression unparsed
      Include fail test strings as the form "Test failed for parseE on {testE}"
    """
    test_cases = [
        (23, expr(numExpr(23))),
        (['+', 1, 2], 
         expr(appExpr(op('+'), [numExpr(1), numExpr(2)]))),
        (['-', 10, 20, -10], 
         expr(appExpr(op('-'), [numExpr(10), numExpr(20), numExpr(-10)]))),
        (['*', 1, 2, 3, 4, 5], 
         expr(appExpr(op('*'), [numExpr(1), numExpr(2), numExpr(3), numExpr(4), 
                                numExpr(5)]))),
        (['/', 12, 4, 3], 
         expr(appExpr(op('/'), [numExpr(12), numExpr(4), numExpr(3)]))),
        ([['lam', ['x'], ['*', 'x', 'x']], 10], 
         expr(appExpr(lam(['x'], expr(appExpr(op('*'), [varExpr('x'), varExpr('x')]))), 
                      [numExpr(10)]))),
        ([['lam', ['x', 'y'], ['+', ['*', 'x', 'x'], ['/', 'y', 2]]], 5, 4],
         expr(appExpr(lam(['x', 'y'],
                          expr(appExpr(op('+'), 
                                       [appExpr(op('*'), [varExpr('x'), varExpr('x')]), 
                                        appExpr(op('/'), [varExpr('y'), numExpr(2)])]))), 
                          [numExpr(5), numExpr(4)])))
    ]
    for testE, expected in test_cases:
        result = parseE(testE)
        assert result.unparse() == expected.unparse(), \
               f"Test failed for parseE on {testE}"

test_parseE()

def eval(concreteE):
    """
    Signature: E -> value
    Purpose: Evaluate the given concrete expression
    Design Idea: Parse the given concrete expression and evaluate using an empty environment
    """
    return parseE(concreteE).eval(Env())

def test_eval():
    """
    Signature:  -> None
    Purpose: test eval
    Design Idea:
      Use the concrete grammar to generate concrete expressions
      Generate 2 concrete expressions that are numE
      Generate 4 concrete expressions that are appE using '+', '-'. '*', and '/'
      Generate 2 concrete expressions that are appE using a funct
      For each E generated:
        assert eval(E) == expected value
      Include failed test strings
    """
    test_cases = [
        (23, 23),
        (['+', 1, 2], 3),
        (['-', 10, 20, -10], 0),
        (['*', 1, 2, 3, 4, 5], 120),
        (['/', 12, 4, 3], 1.0),
        ([['lam', ['x'], ['*', 'x', 'x']], 10], 100),
        ([['lam', ['x', 'y'], ['+', ['*', 'x', 'x'], ['/', 'y', 2]]], 5, 4], 27)
    ]
    for expr_obj, expected_value in test_cases:
        result = eval(expr_obj)
        assert result == expected_value, \
               f"Test failed for eval on {expr_obj}, expected {expected_value} but got {result}"

test_eval()

