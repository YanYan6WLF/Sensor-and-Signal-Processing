% 定义 PCB 平面
xPCB = [0 40 40 0];
yPCB = [0 0 40 40];
zPCB = [0 0 0 0];
figure;
fill3(xPCB, yPCB, zPCB, [0.9 0.8 0.7], 'FaceAlpha', 0.5);
hold on;

% 绘制线圈中心
coilCenters = [
    10, 10, 0;  % A
    30, 10, 0;  % B
    10, 30, 0;  % C
    30, 30, 0   % D
];
scatter3(coilCenters(:,1), coilCenters(:,2), coilCenters(:,3), 100, 'filled');
text(coilCenters(:,1), coilCenters(:,2), coilCenters(:,3), {'A', 'B', 'C', 'D'}, 'FontSize', 12, 'Color', 'k');

% 绘制手机传感器位置
sensorPos = [20, 20, 5];
scatter3(sensorPos(1), sensorPos(2), sensorPos(3), 200, 'o', 'MarkerEdgeColor', 'k', 'MarkerFaceColor', 'c');
text(sensorPos(1), sensorPos(2), sensorPos(3), 'Sensor', 'FontSize', 12, 'Color', 'k');

% 绘制磁场矢量
B_noCoil = [0, 0, 1];
B_A = [1, 0, 1];
B_B = [0, 1, 1];
B_C = [-1, 0, 1];
B_D = [0, -1, 1];

quiver3(sensorPos(1), sensorPos(2), sensorPos(3), B_noCoil(1), B_noCoil(2), B_noCoil(3), 0, 'k', 'LineWidth', 2);
quiver3(sensorPos(1), sensorPos(2), sensorPos(3), B_A(1), B_A(2), B_A(3), 0, 'r', 'LineWidth', 2);
quiver3(sensorPos(1), sensorPos(2), sensorPos(3), B_B(1), B_B(2), B_B(3), 0, 'b', 'LineWidth', 2);
quiver3(sensorPos(1), sensorPos(2), sensorPos(3), B_C(1), B_C(2), B_C(3), 0, 'g', 'LineWidth', 2);
quiver3(sensorPos(1), sensorPos(2), sensorPos(3), B_D(1), B_D(2), B_D(3), 0, 'c', 'LineWidth', 2);

% 设置图例
legend({'PCB', 'Coil Centers', 'Sensor Position', 'B_{no-coil}', 'B_A', 'B_B', 'B_C', 'B_D'}, 'Location', 'northeastoutside');

% 设置轴标签和视角
xlabel('X Axis');
ylabel('Y Axis');
zlabel('Z Axis');
title('3D Representation of Smartphone’s Sensor Position on the PCB Board');
grid on;
axis equal;
view(3);
hold off;
