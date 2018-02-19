mkdir matlab
cd mmatlab
Error using cd
Cannot CD to mmatlab (Name is nonexistent or not a directory).
 
cd matlab
% Mērijumu datu apstrāde
Um = [-1 0.3 1.5 2.5 3.2];
Im = [1.1 2.2 2.1 3.2 4.7];
plot(Um,Im, 'o-')
% MĒģināsim atminēt sakarību, kas sasaista x(Um) un y(Im).
% Sakaeību meklēsim, kā 2. kārtas polinomu
%Koeficentus 2.kārtas polinomus atrodīsim ar POLYFIT funkciju
%Poly - polynomial, Fit - fitting > c = polyfit(x,y,N) N - POlinoma kārta
C = polyfit(Um,Im,2)

C =

    0.1716    0.3662    1.5034

format compact
% norformēšu "x" ar mazāku soli
U = -1:0.01:3.2;
% APRĒĶINA Y 
I = C(1)*U.^2+C(2)*U+C(3);
%zīmēsom grafiku, kas iznāca
plot(Um,Im,'o',U,I)
% atkārtojam to pašu ar 3.k polinomu
C = polyfit(Um,Im,2)
C =
    0.1716    0.3662    1.5034
C = polyfit(Um,Im,3)
C =
    0.1838   -0.4328    0.3391    2.0688
I = C(1)*U.^3+C(2)*U.^2+C(3)*U+C(4);
plot(Um,Im,'o',U,I)
%Atkārtosim 4.k polinomam, izteiksem sastadišana ilga, tāpēc to automatizēsim
%Izmantojot POLYVAL funkciju POLY - POLINOMIAL VAL - VALUE
% y = polyval(C,x); 
%Piemers 3. kārtai
C = polyfit(Um,Im,3);
I = polyval(C,U);
plot(Um,Im,'o',U,I)
C = polyfit(Um,Im,4);
I = polyval(C,U);
plot(Um,Im,'o',U,I)
% Iznak poliomiāla interpolācija - grafiks iet caurn katru punktu precīzi
%Citos gadījumos "aproksimācija" -  negāja
% pie lielas polinoma pakāpes, gan aproksimācijai, gan interpolācijai, radīsies nevelāmas oscilācijas(kļūdas)
C = polyfit(Um,Im,10);
Warning: Polynomial is not unique; degree >= number of data points. 
> In polyfit (line 70) 
I = polyval(C,U);
plot(Um,Im,'o',U,I)

%lineāra sakarība
C = polyfit(Um,Im,1);
I = polyval(C,U);
plot(Um,Im,'o',U,I)

%Vairākas mērījumu sērijas
Um = [-1 0.3 1.5 2.5 3.2];
Im = [1.1 2.2 2.1 3.2 4.7; 
         0.9 1.8 2.6 3.3 4.5;
         1.0 2.0 2.4 3.4 4.3;
         0.8 1.9 2.5 3.5 4.4;
         1.0 2.1 2.2 3.3 4.6];
% Jautājums kā matlab zīmēs matricas?
plot(Um,Im,'o-)
 plot(Um,Im,'o-)
            ↑
Error: Character vector is not terminated properly.
 
figure,plot(Um,Im,'o-')
figure,plot(Um,Im','o-')


% pielaikosim polinomu
% Meklēsim vidējo vērtību
Ivid = mean(Im)
Ivid =
    0.9600    2.0000    2.3600    3.3400    4.5000
C = polyfit(Um,Ivid,3);
U = -1:0.01:3.2;
I = polyval(C,U);
%UZīmet grafiku, lai mērījuma punkti butu ar 'o'─ lai vid starp mērijumiem butu ar '*k'
% lai pielaikotais polinoms butu ar liniju '-'
plot(Um,Im,'o',U,I,'*k',U,Ivid,'-')
Error using plot
Vectors must be the same length. 
figure.plot(Um,Im,'o',U,I,'*k',U,Ivid,'-')
Undefined variable "figure" or class "figure.plot". 
figure,plot(Um,Im,'o',U,I,'*k',U,Ivid,'-')
Error using plot
Vectors must be the same length. 
plot(Um,Im','o',Um,Ivid,'*',U,I,'-')
%Pareizas ^^^, kad ir vairakas mērijuma sērijas, rēķina videjo kvadrātisko novirzi
Ivkn = std(Im)
Ivkn =
    0.1140    0.1581    0.2074    0.1140    0.1581
errorbar(Um,Im,Ivkn)
Error using errorbar>checkSingleInput (line 264)
XData must be the same size as YData.
Error in errorbar (line 94)
x = checkSingleInput(x, sz, 'XData'); 
errorbar(Um,Ivid,Ivkn)
% Kā ielasīt skenēto grafiku un iegūt mērījuma punktus
cd

/home/user/matlab

ls
image1.JPG  image2.JPG

%Ielasīsim bildes matlabā
A = imread('image1.JPG');
B = imread('image2.JPG');
figure(1),image(A),shg
figure(2),image(B),shg
% 2. grafikas uzstadisim īstus x un y vērtības
figure(2),image([0 14],[0 80]B)
 figure(2),image([0 14],[0 80]B)
                              ↑
Error: Unexpected MATLAB expression.
 
figure(2),image([0 14],[0 80],B),
figure(2),image([0 14],[80 0],B),
set(gca,'YDir','normal')
[x,y] = ginput(5)
x =
    4.5275
    5.8203
    8.5998
   11.2824
   13.6418
y =
   18.7345
   27.3809
   36.4947
   41.4021
   44.4401
