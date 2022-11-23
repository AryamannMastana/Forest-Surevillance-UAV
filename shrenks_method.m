% Our parameters of our UAV
AR = 10;
e = 0.79;
S = 0.484;
b = 2.2;
chord_root = 0.294;
chord_tip = 0.147;
step_size = b/200;

% Chord Distribution of an equivalent(span and area same) Elliptic Distribution
c_ellipse = [];
for i = 1:100
    y = (i-1)*step_size;
    c_ellipse(i) = (4*S/(pi*b))*sqrt(1 - (2*y/b)^2);
end
c_ellipse;

% Chord Distribution of our designed UAV
c_actual = [];
for i = 1:100
    y = (i-1)*step_size;
    c_actual(i) = chord_root + ((chord_root - chord_tip)/(0-b))*y;
end

% Shrenk's Method Chord Distribution:
c_shrenk = (c_actual + c_ellipse)*0.5;
X = 0:step_size:b/2-step_size;
plot(X,c_shrenk)
hold on  
plot(X,c_actual)
plot(X,c_ellipse)
legend('shrenk','actual','ellipse');

xlabel("Span-wise location y/(b/2)");
ylabel("Mean Aerodynamic Chord c(y) (m)");
title("Schrenk's method")

hold off
grid on