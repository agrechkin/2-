height = int(input())
weight = int(input())

imt = weight / (height**2 / 100)

if imt < 16:
    print('выраженный дефецит массы тела')
if 16 <= imt < 18.5:
    print('достаточная масса тела')
if 18.5 <= imt < 25:
    print('норма')
if 25 <= imt < 30:
    print('избыточная масса тела')
if 30 <= imt < 35:
    print('ожирение первой степени')
if 35 <= imt < 40:
    print('ожирение второй степени')
if imt >= 40:
    print('ожирение третьей степени')