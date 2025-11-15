# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

# Datos medidos
I = 0.1015  # A
VR = 5.18   # V (tension en resistencia externa)
VZL = 8.75  # V (tension en la bobina)
VT = 12.55  # V (tension total)
R = 51.5    # Ohm (resistencia externa)

# Parametros calculados de la bobina
r = 50.7    # Ohm (resistencia interna)
L = 0.22    # H (inductancia)
f = 50      # Hz
omega = 2 * np.pi * f

# Calculos
XL = omega * L  # Reactancia inductiva
Vr = I * r      # Tension resistiva en la bobina
VL = I * XL     # Tension inductiva en la bobina

# Angulo de desfase
phi = np.arctan(VL / (VR + Vr))  # Angulo entre VT e I (referencia)
phi_grados = np.degrees(phi)

# Crear figura
fig, ax = plt.subplots(figsize=(10, 8))

# Configurar ejes
ax.set_xlim(-2, 14)
ax.set_ylim(-2, 10)
ax.set_aspect('equal')
ax.axhline(y=0, color='k', linewidth=0.5)
ax.axvline(x=0, color='k', linewidth=0.5)
ax.grid(True, alpha=0.3)

# Dibujar vectores (fasores)
# Tomamos I como referencia en el eje real (fase 0 grados)

# VR: tension en resistencia externa (en fase con I)
ax.arrow(0, 0, VR, 0, head_width=0.3, head_length=0.4, fc='blue', ec='blue', linewidth=2)
label_VR = 'VR = {:.2f} V'.format(VR)
ax.text(VR/2, -0.6, r'$' + label_VR.replace('VR', 'V_R') + r'$', fontsize=11, ha='center', color='blue', weight='bold')

# Vr: tension en resistencia interna (en fase con I, continua desde VR)
ax.arrow(VR, 0, Vr, 0, head_width=0.3, head_length=0.4, fc='green', ec='green', linewidth=2)
label_Vr = 'Vr = {:.2f} V'.format(Vr)
ax.text(VR + Vr/2, -0.6, r'$' + label_Vr.replace('Vr', 'V_r') + r'$', fontsize=11, ha='center', color='green', weight='bold')

# VL: tension inductiva (perpendicular, desde el final de Vr)
ax.arrow(VR + Vr, 0, 0, VL, head_width=0.3, head_length=0.4, fc='red', ec='red', linewidth=2)
label_VL = 'VL = {:.2f} V'.format(VL)
ax.text(VR + Vr + 0.8, VL/2, r'$' + label_VL.replace('VL', 'V_L') + r'$', fontsize=11, ha='left', color='red', weight='bold')

# VZL: tension total en la bobina (desde origen hasta el final de Vr + VL)
ax.arrow(0, 0, VR + Vr, VL, head_width=0.3, head_length=0.4, fc='purple', ec='purple', 
         linewidth=2.5, linestyle='--', alpha=0.7)
label_VZL = 'VZL = {:.2f} V'.format(VZL)
ax.text((VR + Vr)/2 - 1, VL/2 + 0.5, r'$' + label_VZL.replace('VZL', 'V_{ZL}') + r'$', 
        fontsize=12, ha='center', color='purple', weight='bold')

# Verificar VT (deberia ser aproximadamente igual a VZL + VR vectorialmente)
# En este caso VT = sqrt((VR + Vr)^2 + VL^2)
VT_calculado = np.sqrt((VR + Vr)**2 + VL**2)

# Dibujar VT desde el origen
ax.arrow(0, 0, VR + Vr, VL, head_width=0, head_length=0, fc='orange', ec='orange', 
         linewidth=3, alpha=0.5)
label_VT = 'VT aprox {:.2f} V\n(medido: {} V)'.format(VT_calculado, VT)
ax.text((VR + Vr)/2 + 1.5, VL/2 - 0.8, r'$' + label_VT.split('\n')[0].replace('VT aprox', 'V_T \\approx') + r'$' + '\n(medido: {} V)'.format(VT), 
        fontsize=11, ha='center', color='orange', weight='bold', 
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# Marcar el angulo phi
angle_arc = np.linspace(0, phi, 30)
arc_radius = 2.5
ax.plot(arc_radius * np.cos(angle_arc), arc_radius * np.sin(angle_arc), 'k-', linewidth=1.5)
label_phi = 'phi = {:.1f} grados'.format(phi_grados)
ax.text(arc_radius + 0.5, 0.8, r'$\varphi = ' + '{:.1f}'.format(phi_grados) + r'^{\circ}$', fontsize=12, weight='bold')

# Etiquetas de ejes
ax.set_xlabel('Eje Real (V)', fontsize=12, weight='bold')
ax.set_ylabel('Eje Imaginario (V)', fontsize=12, weight='bold')
ax.set_title('Diagrama de Fasores - Circuito Serie R-L', fontsize=14, weight='bold')

# Leyenda
legend_elements = [
    plt.Line2D([0], [0], color='blue', linewidth=2, label=r'$V_R$ (tension en R externa)'),
    plt.Line2D([0], [0], color='green', linewidth=2, label=r'$V_r$ (tension en r interna)'),
    plt.Line2D([0], [0], color='red', linewidth=2, label=r'$V_L$ (tension inductiva)'),
    plt.Line2D([0], [0], color='purple', linewidth=2.5, linestyle='--', label=r'$V_{ZL}$ (tension en bobina)'),
    plt.Line2D([0], [0], color='orange', linewidth=3, alpha=0.5, label=r'$V_T$ (tension total)')
]
ax.legend(handles=legend_elements, loc='upper left', fontsize=10)

# Agregar anotaciones con coordenadas
coordenadas_text = 'Coordenadas (Real, Imaginaria):\n'
coordenadas_text += 'VR: ({:.2f}, 0)\n'.format(VR)
coordenadas_text += 'Vr: ({:.2f}, 0) desde VR\n'.format(Vr)
coordenadas_text += 'VL: (0, {:.2f}) desde VR+Vr\n'.format(VL)
coordenadas_text += 'VZL: ({:.2f}, {:.2f})'.format(VR + Vr, VL)

ax.text(0.5, 8.5, coordenadas_text, fontsize=9, 
        bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8),
        verticalalignment='top')

plt.tight_layout()
plt.savefig('/Users/tomaspinausig/Desktop/f3/tp4_f3/imagen/diagrama_fasores.png', dpi=300, bbox_inches='tight')
print("Diagrama de fasores generado exitosamente: imagen/diagrama_fasores.png")
print("\nValores calculados:")
print("Vr = {:.2f} V".format(Vr))
print("VL = {:.2f} V".format(VL))
print("VZL calculado = sqrt(Vr^2 + VL^2) = {:.2f} V (medido: {} V)".format(np.sqrt(Vr**2 + VL**2), VZL))
print("VT calculado = sqrt((VR+Vr)^2 + VL^2) = {:.2f} V (medido: {} V)".format(VT_calculado, VT))
print("Angulo phi = {:.1f} grados".format(phi_grados))
