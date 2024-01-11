% Parameters for muscle shape
length = 4;         % Length of the muscle
radius = 1;         % Radius of the muscle
theta = linspace(0, pi, 100);
phi = linspace(0, 2*pi, 100);
[theta, phi] = meshgrid(theta, phi);

% Parametric equations for the muscle shape
x = length * sin(theta) .* cos(phi);
y = length * sin(theta) .* sin(phi);
z = radius * cos(theta);

% Create a mesh plot
figure;
surf(x, y, z, 'FaceColor', 'red', 'EdgeColor', 'none');
title('Muscle Mesh Plot');
xlabel('X-axis');
ylabel('Y-axis');
zlabel('Z-axis');
axis equal;
grid on;

% Add lighting for better visualization
light('Position', [1, 1, 1]);
lighting gouraud;
