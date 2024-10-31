x = int(input('How many students on the course?'))
y = int(input('Desired group size?'))

product = (x // -y)
if product < 1 :
    print(f'Number of groups formed: {product *-1}')