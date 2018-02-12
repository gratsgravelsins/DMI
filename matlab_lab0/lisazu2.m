function lisazu2(f1,f2)
% Skripts, kas zimes lisazu figuras(parametriskas)
t = 0:0.01:1;
%f1 = 69; f2 = 69;
for faze = 0:pi/100:4*pi
x = cos(2*pi*f1*t+faze);
y = sin(2*pi*f2*t);
plot(x,y)
pause(0.01)
end
%pirmaja verisija f1 = 1 un f2 = 2