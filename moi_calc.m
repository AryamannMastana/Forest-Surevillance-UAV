% Our parameters of our UAV
AR = 10;
e = 0.79;
S = 0.484;
b = 2.2;
chord_root = 0.294;
chord_tip = 0.147;
step_size = b/200;
g = 9.81;
W = S*155.59;
stress = 450 * 10^6;
thickness = 0.5*10^-3;

% Chord Distribution of an equivalent(span and area same) Elliptic Distribution
c_ellipse = [];
for i = 1:101
    y = (i-1)*step_size;
    c_ellipse(i) = (4*S/(pi*b))*sqrt(1 - (2*y/b)^2);
end
c_ellipse;

% Chord Distribution of our designed UAV
c_actual = [];
for i = 1:101
    y = (i-1)*step_size;
    c_actual(i) = chord_root + ((chord_root - chord_tip)/(0-b/2))*y;
end

%Shrenk's Method Chord Distribution:
c_shrenk = (c_actual + c_ellipse)*0.5;
X = 0:step_size:b/2;

figure(1)
plot(X,c_shrenk)
hold on  
plot(X,c_actual)
plot(X,c_ellipse)
legend('shrenk','actual','ellipse');
xlabel("Span (y)");
ylabel("Mean Aerodynamic Chord (m)");
title("Shrenk Lift Distribution")
hold off
grid on

% Lift Distribution :
X = 0:step_size:b/2;
local_lift_coefficient = c_shrenk./c_actual;

figure(2)
plot(X,local_lift_coefficient)
ylim([0.4,1.1])
xlabel("Span (y)");
ylabel("Local Lift Coefficient");
title("Local Lift Coefficient for unit CL vs span")
grid on

% Also make sure that the integral of Lift equals W/2 for the one wing:
sum_lift = 0;
shear_force = [];
for i = 1:101
    y = (i-1)*step_size;
    sum_lift = sum_lift + local_lift_coefficient(i)*step_size;
    shear_force(i) = sum_lift;
end
kappa = W/(2*sum_lift)
actual_lift = kappa*local_lift_coefficient;

figure(3)
plot(X,actual_lift)
xlabel("Span (y)");
ylabel("Lift Distribution");
title("Lift as a function of span")
grid on

% Shear Force as a function of span:
dL_dy = diff(actual_lift)/step_size;
shear_force = kappa*fliplr(shear_force);

figure(4)
plot(X,shear_force)
xlabel("Span (y)");
ylabel("Shear Force");
title("Shear Force as a function of span")
grid on

% Bending Moment as a function of span:
sum_moment = 0;
bending_moment = [];
for i = 1:101
    y = (i-1)*step_size;
    sum_moment = sum_moment + shear_force(i)*y;
    bending_moment(i) = sum_moment;
end
bending_moment = fliplr(bending_moment);
bending_moment = bending_moment - bending_moment(1);

figure(5)
plot(X,bending_moment)
xlabel("Span (y)");
ylabel("Bending Moment");
title("Bending Moment as a function of span")
grid on

% Spar width as a function of span:
moment_of_inertia = [];
for i = 1:101
    y = (i-1)*step_size;
    moment_of_inertia(i) = bending_moment(i)*c_actual(i)/stress;
end

figure(6)
plot(X,moment_of_inertia)
xlabel("Span (y)");
ylabel("Moment Of Inertia");
title("Moment of Inertia as a function of span")
grid on

figure(7)
spar_width = moment_of_inertia*2/(thickness^2);
plot(X,spar_width)
xlabel("Span (y)");
ylabel("Spar Width");
title("Spar Width as a function of span")
grid on