<?php
$db_file = '/tmp/nexacore_hr.db';

try {
    $pdo = new PDO('sqlite:' . $db_file);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $pdo->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

function init_database($pdo) {
    $pdo->exec("CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL DEFAULT 'employee'
    )");

    $pdo->exec("CREATE TABLE IF NOT EXISTS hr_records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        employee_id TEXT NOT NULL,
        name TEXT NOT NULL,
        department TEXT NOT NULL,
        notes TEXT
    )");

    $pdo->exec("CREATE TABLE IF NOT EXISTS audit_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT NOT NULL,
        user TEXT NOT NULL,
        action TEXT NOT NULL
    )");

    $count = $pdo->query("SELECT COUNT(*) FROM users")->fetchColumn();
    if ($count == 0) {
        $stmt = $pdo->prepare("INSERT INTO users (username, password, role) VALUES (?, ?, ?)");
        $stmt->execute(['admin', 'N3x4C0r3_Admin_2026!', 'admin']);
        $stmt->execute(['avance', 'employee123', 'employee']);
        $stmt->execute(['svance', 'employee123', 'employee']);
    }

    $count = $pdo->query("SELECT COUNT(*) FROM hr_records")->fetchColumn();
    if ($count == 0) {
        $stmt = $pdo->prepare("INSERT INTO hr_records (employee_id, name, department, notes) VALUES (?, ?, ?, ?)");
        $stmt->execute(['IT24102409', 'Alex Vance', 'Systems Engineering', 'Terminated - access revoked']);
        $stmt->execute(['IT24101383', 'Sarah Chandrasekara', 'HR', 'Active']);
        $stmt->execute(['IT24103169', 'Mishan Avishka', 'Security', 'Active']);
        $stmt->execute(['IT24103344', 'Dilan Wickramasinghe', 'IT Support', 'Active']);
    }

    $count = $pdo->query("SELECT COUNT(*) FROM audit_logs")->fetchColumn();
    if ($count == 0) {
        $stmt = $pdo->prepare("INSERT INTO audit_logs (timestamp, user, action) VALUES (?, ?, ?)");
        $stmt->execute(['2026-03-15 02:34:11', 'avance', 'Login successful']);
        $stmt->execute(['2026-03-15 02:45:23', 'avance', 'Exported HR records']);
        $stmt->execute(['2026-03-15 03:12:07', 'avance', 'Created backup account']);
        $stmt->execute(['2026-03-15 03:45:55', 'avance', 'Deleted audit logs']);
        $stmt->execute(['2026-03-16 09:00:00', 'admin', 'Account revoked: avance']);
    }
}

init_database($pdo);
?>
