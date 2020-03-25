def main(*args):
  total = 0
  for i in args:
    total = total + i
  return total

#print(multi_add(4,3,2,2))


if __name__ == '__main__':
    main()
print(main(2,3,5,4))