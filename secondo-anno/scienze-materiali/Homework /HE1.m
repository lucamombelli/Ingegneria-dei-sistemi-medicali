% Caricare i dati
clc;
clearvars;
data = readmatrix('HE1.txt');

% Separare le colonne
theta = data(:, 1);
intensity = data(:, 2);

% Trovare il picco più alto
[max_intensity, idx] = max(intensity);
peak_theta = theta(idx);

% Creare il grafico
figure;
plot(theta, intensity, 'r', 'LineWidth', 1);
hold on;

% Aggiungere una linea di base magenta
yline(0, 'm', 'LineWidth', 1);

% Evidenziare il picco più alto
text(peak_theta, max_intensity, sprintf('(%0.2f, %0.2f)', peak_theta, max_intensity), ...
    'FontSize', 12, 'FontWeight', 'bold', 'HorizontalAlignment', 'left', 'VerticalAlignment', 'bottom');

% Etichette
xlabel('2 theta (degree)');
ylabel('Intensity');
title('XRD Pattern');

% Mostrare il valore del picco nel Command Window
fprintf('Il picco più alto si trova a 2θ = %.2f° con un intesita di %.2f.\n', peak_theta, max_intensity);