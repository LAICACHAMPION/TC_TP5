clear all
clearvars;
clc;

M = csvread('Simulacion_comun_bode.csv');

Frec = M(:,1)
Mag = M(:,2);
Pha = M(:,3);


semilogx(Frec, Mag)
xlabel('Frequency (Hz)')
ylabel('Magnitude (dB)')
Frec(1)
log(Frec(1))
log(Frec(length(Frec)))



% #Digilent WaveForms Network Analyzer - Bode
% #Device Name: Discovery2
% #Serial Number: SN:210321A35FCC
% #Date Time: 2018-10-29 18:31:51.647
% #Start: 1000 Hz
% #Stop: 1e+06 Hz
% #Steps: 100
% #Wavegen: Wavegen1
% #Amplification: 1 X
% #Settle: 10 ms
% #MinPeriods: 16
% #Channel: Channel 1
% #Range: 5.42537 V
% #Offset: 0.000183761 V
% #Relative: no
% #Channel: Channel 2
% #Range: 5.47028 V
% #Offset: -7.92091e-07 V
% #Relative: yes
% Frequency (Hz),Channel 1 Magnitude (dB),Channel 2 Magnitude (dB),Channel 2 Phase (°)

hold on
M2 = csvread('default.csv');

Frec2 = M2(:,1)
Mag1 = M2(:,2);
Mag2 = M2(:,3);
Pha2 = M2(:,4);

semilogx(Frec2, Mag2)
xlim([1000 Frec(length(Frec))])
ylim([-100 10])

