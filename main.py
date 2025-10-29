from js import document


def euro_convert(num_input1):
    try:
        input_euro = document.getElementById("euro_input")
        output_euro = document.getElementById("euro_output")

        num_input1 = float(input_euro.value)
        result = num_input1 * 1.95583

        output_euro.innerText = f"{result:.2f} лв"
        print(num_input1, "=", result)
    except ValueError:
        output_euro.innerText = "⚠️ Моля, използвайте само числа !"


def bgn_convert(num_input1):
    try:
        input_bgn = document.getElementById("bgn_input")
        output_bgn = document.getElementById("bgn_output")

        num_input1 = float(input_bgn.value)
        result = num_input1 * 0.51

        output_bgn.innerText = f"{result:.2f} €"
        print(num_input1, "=", result)

    except ValueError:
        output_bgn.innerText = "⚠️ Моля, използвайте само числа!"

# try:
#     def euro(num1):
#         return num1 * 1.96
#
#
#     num1 = int(input("Моля, въведете сума! "))
#     print(num1, "=", euro(num1))
#
#
#     def bgn(num1):
#         return num1 * 0.51
#
#
#     num1 = int(input("Моля, въведете сума! "))
#     print(num1, "=", bgn(num1))
#
#     num1 = int(num1)
# except ValueError:
#     raise ValueError("Моля, използвайте само числа !")
