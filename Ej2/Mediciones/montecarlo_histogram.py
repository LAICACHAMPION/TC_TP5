import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rc
rc('text', usetex=True)


path = "Funciona_montecarlo.txt"

f = []
mag = []
mag1 = []
mag2 = []
mag3 = []

bw = []
f1 = []
f2 = []
f3 = []

input = open(path, "r")
if not input.mode == "r":
    print("esta mal el path gil")

line = input.readline()  # descarto la linea "Freq.	V(out)	V(out)/V(s2)	V(s1)	V(s2)/V(s1)"
line = input.readline()  # descarto el step information
line = input.readline()

while len(line):  # solo se devuelve vacio si llegue al EOF
    while len(line):
        if not line[0].isdigit():
            break
        freq, line = line.split("\t(", 1)
        f.append(float(freq))
        m, line = line.split('d', 1)
        mag.append(float(m))
        line = input.readline()

    a = next((m for m in mag if m < -3), None)
    if a is not None:
        bw.append(f[mag.index(a)])

    a = next((m for m in mag if m < -40), None)
    if a is not None:
        f.append(f[mag.index(a)])

    f.clear()
    mag.clear()

    line = input.readline()


fig = sns.distplot(bw)
y_vals = fig.get_yticks()
sum = 0
for i in y_vals:
    sum += i
factor = 1/sum
fig.set_yticklabels(['{:3.0f}%'.format(x * factor * 100) for x in y_vals])

#plt.savefig("histograma_marce.png")
plt.title('Ancho de banda')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Probabilidad')
plt.grid(True)
plt.show()

fig = sns.distplot(f1)
y_vals = fig.get_yticks()
sum = 0
for i in y_vals:
    sum += i
factor = 1/sum
fig.set_yticklabels(['{:3.0f}%'.format(x * factor * 100) for x in y_vals])

#plt.savefig("histograma_marce.png")
plt.title('Polo primera etapa')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Probabilidad')
plt.grid(True)
plt.show()


fig = sns.distplot(f2)
y_vals = fig.get_yticks()
sum = 0
for i in y_vals:
    sum += i
factor = 1/sum
fig.set_yticklabels(['{:3.0f}%'.format(x * factor * 100) for x in y_vals])

#plt.savefig("histograma_marce.png")
plt.title('Polo segunda etapa')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Probabilidad')
plt.grid(True)
plt.show()


fig = sns.distplot(f3)
y_vals = fig.get_yticks()
sum = 0
for i in y_vals:
    sum += i
factor = 1/sum
fig.set_yticklabels(['{:3.0f}%'.format(x * factor * 100) for x in y_vals])

#plt.savefig("histograma_marce.png")
plt.title('Polo tercera etapa')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Probabilidad')
plt.grid(True)
plt.show()
# n, bins, _ = plt.hist(bw)
# plt.xlabel('Frecuencia (Hz)')
# plt.ylabel('Probabilidad')
# plt.grid(True)
# plt.show()
#
#
# n, bins, _ = plt.hist(f1)
# plt.xlabel('Frecuencia (Hz)')
# plt.ylabel('Probabilidad')
# plt.grid(True)
# plt.show()
#
# n, bins, _ = plt.hist(f2)
# plt.xlabel('Frecuencia (Hz)')
# plt.ylabel('Probabilidad')
# plt.grid(True)
# plt.show()
#
#
# n, bins, _ = plt.hist(f3)
# plt.xlabel('Frecuencia (Hz)')
# plt.ylabel('Probabilidad')
# plt.grid(True)
# plt.show()