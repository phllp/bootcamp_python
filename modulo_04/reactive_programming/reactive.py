import rx
from rx import operators as ops

from functional import seq


# lambda x, y: x + y
# lambda y,x : x * y
# lambda x, y: x * y

result = seq("Ram", "Mohan", "Shyam").map(lambda input: "Received " + input + "\n").reduce(lambda x, y: x + y)
print(result)