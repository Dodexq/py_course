dice_rolls_a = [(a,b,c,d,e)
                for a in range(1, 7)
                for b in range(1, 7)
                for c in range(1, 7)
                for d in range(1, 7)
                for e in range(1, 7)]

print(dice_rolls_a, "Len list comp = ", len(dice_rolls_a))

dice_rolls_b = [(a,b,c,d,e)
                for a in range(1, 7)
                for b in range(a, 7)
                for c in range(b, 7)
                for d in range(c, 7)
                for e in range(d, 7)]

print(dice_rolls_b, "Len uniq list comp = ", len(dice_rolls_b))