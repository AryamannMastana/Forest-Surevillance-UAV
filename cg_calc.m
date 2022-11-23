clc; clear; close all;

rho = 1.225;
K = 0.0355;
C_D_0 = 0.0219;
S = 1.962;
W = 8;

v = linspace(0.1,40,1000);

C_L = 2 * W ./ (rho .* v.^2 * S);

C_D = C_D_0 + K * 100 * C_L.^2;

P_R = 1/2 * rho * S * v.^3 .* C_D; 
P_A = 553;

figure(1);

plot(v,P_R,'b-');
hold on
yline(P_A,'r--');
hold off
grid();
xlim([0,35]);
ylim([0,1500]);
title('Power Available vs. Power Required');
xlabel('Velocity (m/s)');
ylabel('Power (W)');
legend(['Power Required'],['Power Available']);








