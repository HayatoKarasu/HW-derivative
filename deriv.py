from matplotlib import pyplot as plt

plt.text(0.01, 0.9, '1) Производная функции - это скорость', fontsize=15)
plt.text(0.01, 0.8, 'изменения функции в определённой точке.', fontsize=15)

fig = plt.gca()
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)

plt.show()

form = r"$a) (a^7)' = 7a^6$"
plt.text(0.01, 0.9, '2) Вычислить производную:', fontsize=15)
plt.text(0.01, 0.8, form, fontsize=15)
plt.text(0.01, 0.7, "Использовали формулу:", fontsize=15)
form = r"$(x^a)' = ax^{a-1}$"
plt.text(0.01, 0.6, form, fontsize=15)

fig = plt.gca()
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)

plt.show()

form = r"$б) (7+3x^2)$"
plt.text(0.01, 0.9, form, fontsize=15)
plt.text(0.01, 0.8, "Используем формулу:", fontsize=15)
form = r"$(au + bv)' = a*u' + b*v'$"
plt.text(0.01, 0.7, form, fontsize=15)
plt.text(0.01, 0.6, "Производная произведения константы", fontsize=15)
plt.text(0.01, 0.5, "на функцию есть произведение этой", fontsize=15)
plt.text(0.01, 0.4, "константы на производную этой функции.", fontsize=15)
form = r"$3*(x^2)' + (7)' = 3*2*x+0 = 6x$"
plt.text(0.01, 0.3, form, fontsize=15)
plt.text(0.01, 0.2, "Для (x) использовали формулу:", fontsize=15)
form = r"$(x^a)' = ax^{a-1}$"
plt.text(0.01, 0.1, form, fontsize=15)
plt.text(0.01, 0.01, "А для (7) формулу: (с)' = 0", fontsize=15)

fig = plt.gca()
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)

plt.show()

form = r"$в) (- \frac{1}{x^2})$"
plt.text(0.01, 0.9, form, fontsize=15)
plt.text(0.01, 0.8, "Используем формулу:", fontsize=15)
form = r"$(cu)' = c*u'$"
plt.text(0.01, 0.7, form, fontsize=15)
plt.text(0.01, 0.6, "Производная произведения константы", fontsize=15)
plt.text(0.01, 0.5, "на функцию есть произведение этой", fontsize=15)
plt.text(0.01, 0.4, "константы на производную этой функции.", fontsize=15)
form = r"$-1*(\frac{1}{x^2})'$"
plt.text(0.01, 0.3, form, fontsize=15)
plt.text(0.01, 0.2, "Для (x) используем формулу:", fontsize=15)
form = r"$(x^a)' = ax^{a-1}$"
plt.text(0.01, 0.1, form, fontsize=15)
form = r"$-1*(\frac{1}{2*x})' = -(-2)*\frac{1}{x^3} = \frac{2}{x^3}$"
plt.text(0.01, 0.025, form, fontsize=15)

fig = plt.gca()
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)

plt.show()

plt.text(0.01, 0.9, '3) Частная производная - это производная', fontsize=15)
plt.text(0.01, 0.8, 'по одной переменной в случае, если', fontsize=15)
plt.text(0.01, 0.7, 'функция имеет несколько переменных.', fontsize=15)

fig = plt.gca()
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)

plt.show()

plt.text(0.01, 0.9, "Вычислить:", fontsize=15)
form = r"$Z'_x = (3x+8y-2x^2y)'_x=3(x)'+(8y)-2y(x^2)'=$"
plt.text(0.01, 0.8, form, fontsize=15)
form = r"$=3(x)'-2y(x^2)'= 3 - 2y2x = 3-4xy'$"
plt.text(0.01, 0.7, form, fontsize=15)
form = r"$Z'_y = (3x+8y-2x^2y)'_x=(3x)+8(y)'-2x^2(y)'=$"
plt.text(0.01, 0.6, form, fontsize=15)
form = r"$=8(y)'-2x^2(y)'= 8-2x^2$"
plt.text(0.01, 0.5, form, fontsize=15)
plt.text(0.01, 0.4, 'Для вычисления использовали формулы:', fontsize=15)
form = r"$(x^a)' = ax^{a-1} и (с)' = 0$"
plt.text(0.01, 0.3, form, fontsize=15)
plt.text(0.01, 0.2, 'для переменной (x) не учитывается (y),', fontsize=15)
plt.text(0.01, 0.1, 'а для переменной (y) не учитывается (x).', fontsize=15)

fig = plt.gca()
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)

plt.show()