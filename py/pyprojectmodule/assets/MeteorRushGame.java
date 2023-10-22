package assets;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.Random;

public class MeteorRushGame extends JFrame implements KeyListener {
    private static final long serialVersionUID = 1L;
    private static final int WINDOW_WIDTH = 1335;
    private static final int WINDOW_HEIGHT = 768;

    private ImageIcon backgroundIcon;
    private ImageIcon playerIcon;
    private ImageIcon obstacleIcon;
    private ImageIcon gameOverIcon;

    private JLabel backgroundLabel;
    private JLabel playerLabel;
    private JLabel obstacleLabel;
    private JLabel gameOverLabel;

    private int playerX;
    private int playerY;
    private int playerSpeed;

    private int obstacleX;
    private int obstacleY;
    private int obstacleSpeed;

    private int score;
    private int level;
    private int maxScore;
    private int maxLevel;
    private boolean gamePaused;
    private boolean gameOver;
    private boolean showPopup;
    private boolean flag3;
    private boolean end1;

    private long popupStartTime;
    private long popupDuration;

    public MeteorRushGame() {
        setTitle("Meteor Rush Game");
        setSize(WINDOW_WIDTH, WINDOW_HEIGHT);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setResizable(false);
        setLocationRelativeTo(null);

        backgroundIcon = new ImageIcon("background.jpg");
        playerIcon = new ImageIcon("player02.png");
        obstacleIcon = new ImageIcon("obstacle.png");
        gameOverIcon = new ImageIcon("game_over.jpg");

        backgroundLabel = new JLabel(backgroundIcon);
        playerLabel = new JLabel(playerIcon);
        obstacleLabel = new JLabel(obstacleIcon);
        gameOverLabel = new JLabel(gameOverIcon);

        playerX = WINDOW_WIDTH / 2 - playerIcon.getIconWidth() / 2;
        playerY = WINDOW_HEIGHT - playerIcon.getIconHeight() - 30;
        playerSpeed = 5;
        if (playerX > 300) {
            obstacleX = new Random().nextInt(playerX - 300) + playerX + 300;
        } else {
            // Handle the case when playerX is too small to compute a valid bound.
            obstacleX = new Random().nextInt(300) + 1;
            // You can set obstacleX to a default value or handle it in another way.
        }
        
        
        obstacleY = -obstacleIcon.getIconHeight();
        obstacleSpeed = 4;

        score = 0;
        level = 1;
        maxScore = 10;
        maxLevel = 5;
        gamePaused = false;
        gameOver = false;
        showPopup = false;
        flag3 = false;
        end1 = false;

        popupStartTime = 0;
        popupDuration = 5000; // in milliseconds

        setLayout(null);

        backgroundLabel.setBounds(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT);
        playerLabel.setBounds(playerX, playerY, playerIcon.getIconWidth(), playerIcon.getIconHeight());
        obstacleLabel.setBounds(obstacleX, obstacleY, obstacleIcon.getIconWidth(), obstacleIcon.getIconHeight());

        add(backgroundLabel);
        add(playerLabel);
        add(obstacleLabel);

        addKeyListener(this);

        Timer gameTimer = new Timer(16, new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                updateGame();
                repaint();
            }
        });

        gameTimer.start();
    }

    private void updateGame() {
        if (!gameOver) {
            if (!gamePaused) {
                obstacleY += obstacleSpeed;

                if (obstacleY + obstacleIcon.getIconHeight() >= playerY &&
                        obstacleX + obstacleIcon.getIconWidth() >= playerX &&
                        obstacleX <= playerX + playerIcon.getIconWidth()) {
                    gameOver = true;
                }

                if (obstacleY > WINDOW_HEIGHT) {
                    score++;

                    obstacleX = new Random().nextInt(playerX - 300) + playerX + 300;
                    obstacleY = -obstacleIcon.getIconHeight();

                    if (score > maxScore && level < maxLevel) {
                        level++;
                        maxScore += 10;
                        obstacleSpeed++;
                        showPopup = true;
                        popupStartTime = System.currentTimeMillis();
                    } else if ((level == 5 || level == 10 || level == 15) && score > 50) {
                        flag3 = true;
                        popupStartTime = System.currentTimeMillis();
                    }
                }
            }

            playerLabel.setBounds(playerX, playerY, playerIcon.getIconWidth(), playerIcon.getIconHeight());
            obstacleLabel.setBounds(obstacleX, obstacleY, obstacleIcon.getIconWidth(), obstacleIcon.getIconHeight());

            if (showPopup) {
                gamePaused = true;
                long currentTime = System.currentTimeMillis();
                long popupElapsed = currentTime - popupStartTime;

                if (popupElapsed >= popupDuration) {
                    showPopup = false;
                    gamePaused = false;
                }
            }

            if (flag3) {
                gamePaused = true;
                long currentTime = System.currentTimeMillis();
                long popupElapsed = currentTime - popupStartTime;

                if (popupElapsed >= popupDuration) {
                    flag3 = false;
                    if (level >= 15) {
                        end1 = true;
                    }
                }
            }

            if (obstacleX < 0) {
                obstacleX = 0;
            }
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                MeteorRushGame game = new MeteorRushGame();
                game.setVisible(true);
            }
        });
    }

    @Override
    public void keyPressed(KeyEvent e) {
        int key = e.getKeyCode();

        if (key == KeyEvent.VK_LEFT && playerX > 0) {
            playerX -= playerSpeed;
        }
        if (key == KeyEvent.VK_RIGHT && playerX < WINDOW_WIDTH - playerIcon.getIconWidth()) {
            playerX += playerSpeed;
        }
        if (key == KeyEvent.VK_ESCAPE) {
            System.exit(0);
        }
        if (gameOver && key == KeyEvent.VK_R) {
            resetGame();
        }
        if (flag3 && end1 && key == KeyEvent.VK_ENTER) {
            resetGame();
        }
    }

    private void resetGame() {
        gameOver = false;
        score = 0;
        level = 1;
        obstacleSpeed = 4;
        maxScore = 10;
        maxLevel = 5;
        playerX = WINDOW_WIDTH / 2 - playerIcon.getIconWidth() / 2;
        obstacleX = new Random().nextInt(playerX - 300) + playerX + 300;
        gamePaused = false;
        flag3 = false;
        showPopup = false;
        end1 = false;
    }

    @Override
    public void keyReleased(KeyEvent e) {
    }

    @Override
    public void keyTyped(KeyEvent e) {
    }

    @Override
    public void paint(Graphics g) {
        super.paint(g);

        if (gameOver) {
            if (level > 5) {
                if (level >= 10 && level < 15) {
                    // Display appropriate ending message
                    // ...
                } else {
                    // Display appropriate ending message
                    // ...
                }
            } else {
                // Display game over message
                // ...
            }
        }
    }
}
