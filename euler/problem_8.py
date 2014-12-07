# 4 adjacent digits with greatest product are 9989 = 5832
#
# 73167176531330624919225119674426574742355349194934
# 96983520312774506326239578318016984801869478851843
# 85861560789112949495459501737958331952853208805511
# 12540698747158523863050715693290963295227443043557
# 66896648950445244523161731856403098711121722383113
# 62229893423380308135336276614282806444486645238749
# 30358907296290491560440772390713810515859307960866
# 70172427121883998797908792274921901699720888093776
# 65727333001053367881220235421809751254540594752243
# 52584907711670556013604839586446706324415722155397
# 53697817977846174064955149290862569321978468622482
# 83972241375657056057490261407972968652414535100474
# 82166370484403199890008895243450658541227588666881
# 16427171479924442928230863465674813919123162824586
# 17866458359124566529476545682848912883142607690042
# 24219022671055626321111109370544217506941658960408
# 07198403850962455444362981230987879927244284909188
# 84580156166097919133875499200524063689912560717606
# 05886116467109405077541002256983155200055935729725
# 71636269561882670428252483600823257530420752963450
#
# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

def main():

  number_str = '73167176531330624919225119674426574742355349194934' \
    + '96983520312774506326239578318016984801869478851843' \
    + '85861560789112949495459501737958331952853208805511' \
    + '12540698747158523863050715693290963295227443043557' \
    + '66896648950445244523161731856403098711121722383113' \
    + '62229893423380308135336276614282806444486645238749' \
    + '30358907296290491560440772390713810515859307960866' \
    + '70172427121883998797908792274921901699720888093776' \
    + '65727333001053367881220235421809751254540594752243' \
    + '52584907711670556013604839586446706324415722155397' \
    + '53697817977846174064955149290862569321978468622482' \
    + '83972241375657056057490261407972968652414535100474' \
    + '82166370484403199890008895243450658541227588666881' \
    + '16427171479924442928230863465674813919123162824586' \
    + '17866458359124566529476545682848912883142607690042' \
    + '24219022671055626321111109370544217506941658960408' \
    + '07198403850962455444362981230987879927244284909188' \
    + '84580156166097919133875499200524063689912560717606' \
    + '05886116467109405077541002256983155200055935729725' \
    + '71636269561882670428252483600823257530420752963450'

#  number_str = '73167176531330624919225119674426574742355349194934'

  get_greatest_product(number_str)

def get_greatest_product(number_str):
  candidate_lists = _get_candidate_lists(number_str)

  largest_product = 0
  for str_list in candidate_lists:
    candidate_product = greatest_product_no_zeros(str_list)
    if candidate_product > largest_product:
      largest_product = candidate_product

  print 'largest PRODUCT: ' + str(largest_product)


def _get_candidate_lists(number_str):
  no_zero_strings = number_str.split('0')
  candidate_lists = []

  for int_string in no_zero_strings:
    if len(int_string) >= 13:
      candidate_lists.append(int_string)

  return candidate_lists


def greatest_product_no_zeros(number_str):

  print str(number_str)

  #######
  # Get first product
  #######
  list_length = 13
  biggest_prod_range = (0,13)
  next_char_pos = 13

  char_list = list(number_str[biggest_prod_range[0]:biggest_prod_range[1]])
  int_list = map(lambda x: int(x), char_list)

  largest_product = reduce(lambda x, y: x*y, int_list)
  candidate_product = largest_product

  print '=================='
  print 'number_str: ' + number_str
  print 'initial list: ' + str(char_list)
  print 'initial candidate: ' + str(largest_product)

  while next_char_pos < len(number_str):
    next_int = int(number_str[next_char_pos])

    # check if this product bigger than last
    dropped_int = int_list[len(int_list) - list_length]
    candidate_product = (candidate_product / dropped_int) * next_int
    if candidate_product > largest_product:
      biggest_prod_range = (next_char_pos - list_length, next_char_pos)
      largest_product = candidate_product

    int_list.append(next_int)
    next_char_pos += 1

  print 'biggest list: ' + (number_str[biggest_prod_range[0]:biggest_prod_range[1]])
  print 'biggest product: ' + str(largest_product)
  return largest_product

if __name__ == '__main__':
  main()