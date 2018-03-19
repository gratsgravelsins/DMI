function y = lab3demofun(t)
%t = 0:0.01:8;

%t_zero = 0:0.01:1;
t_zerof = (t>=0)&(t<1); t_zero = t(t_zerof);
%t_sin = 1:0.01:2.5;
t_sinf = (t>=1)&(t<2.5); t_sin = t(t_sinf);
%t_noise = 2.5:0.01:4.5;
t_noisef = (t>=2.5)&(t<4.5); t_noise = t(t_noisef);
%t_const = 4.5:0.01:6.5;
t_constf = (t>=4.5)&(t<6.5); t_const = t(t_constf);
%t_saw = 6.5:0.01:8;
t_sawf = (t>=6.5)&(t<=8); t_saw = t(t_sawf);
%% Gabalveida signāla montāža
%% Sinusoīda
%y_sin=A0+A*sin(2*pi*f*(t-sin-delay))
A0=0; % VID vertiba
A=2.5; % Amplituda
T = (2.5-1)/3.5;     
f = 1/T;
delay  = 1;
y_sin=A0+A*sin(2*pi*f*(t_sin-delay));
%plot(t_sin,y_sin)
%% Lineari mainigs signals
%y_saw = k*(t-delay);
% k = (yA-yB)/(tA-tB)
k = (2.5-(-2.5))/(6.5-8);
delay = 7.25;
y_saw = k*(t_saw-delay);
%plot(t_saw,y_saw)
%% Konstante
y_const = 2.5; %šeit ir kļūda
% def y tā lai elementu skaits butu vienāds
%y_const = [2.5 2.5 2.5]%201 reizi jaatkarto
y_const = zeros(1,201)+2.5; % šis ir pareizi, bet tālāk tas varētu dot kļūdu
y_const = zeros(size(t_const))+2.5;
%plot(t_const,y_const)
%% nuļļu signāls 
y_zero = zeros(size(t_zero));
%plot(t_zero,y_zero)
%% Trokšņa signāls
y_noise = 3*rand(size(t_noise))-1.5;
%plot(t_noise,y_noise)
%% Likšana kopā Singālu apvienošana
%t = [t_zero,t_sin,t_noise,t_const,t_saw];
y = [y_zero,y_sin,y_noise,y_const,y_saw];
%plot(t,y)
