<?php
header('Content-Type: application/json');

$csvFile = 'questions.csv';
$questions = [];

if (($handle = fopen($csvFile, 'r')) !== FALSE) {
    while (($data = fgetcsv($handle, 1000, ';')) !== FALSE) {
        $questions[] = [
            'question' => $data[0],
            'options' => [$data[1], $data[2], $data[3]],
            'correct' => $data[1]
        ];
    }
    fclose($handle);
}

$randomQuestion = $questions[array_rand($questions)];
echo json_encode($randomQuestion);
?>
