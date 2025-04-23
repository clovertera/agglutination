import React from "react";
import Card from "react-bootstrap/Card";

interface Feature {
	[key: string]: string | string[];
}

interface WAProps {
	title: string;
	analysis: string;
	list: Feature[];

}

const WordAnalysis: React.FC<WAProps> = ({ title, analysis, list }) => {
	return (
		<Card style={{ width: "400px" }}>
			<Card.Body>
				<Card.Title>{title}</Card.Title>
				<Card.Text>{analysis}</Card.Text>
				<Card.Text>{list}</Card.Text>
			</Card.Body>
		</Card>
	)
}

export default WordAnalysis;
