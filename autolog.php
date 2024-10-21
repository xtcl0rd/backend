<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Get the data sent by the bot
    $data = json_decode(file_get_contents('php://input'), true);
    $message = $data['message'];

    // Append the message to a file (auditlog.txt)
    file_put_contents('auditlog.txt', $message . PHP_EOL, FILE_APPEND);

    // Respond to confirm success
    echo json_encode(["status" => "success"]);
} else {
    // Handle non-POST requests (optional)
    http_response_code(405); // Method Not Allowed
    echo json_encode(["status" => "error", "message" => "Only POST allowed"]);
}
?>
