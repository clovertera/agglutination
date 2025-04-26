import React from "react";
import Card from "react-bootstrap/Card";

interface Feature {
	[key: string]: string | string[];
}

interface WAProps {
	title: string;
	list: Feature[];

}

const WordAnalysis: React.FC<WAProps> = ({ title, list }) => {
	return (
		<Card style={{ width: "600px" }}>
			<Card.Body>
				<Card.Title>{title}</Card.Title>
				<table className="table table-striped table-bordered">
					<thead>
						<tr>
							<th>Feature</th>
							<th>Grammatical Part</th>
							<th></th>
						</tr>
					</thead>
					<tbody>
						{list.flatMap((feature, index) => (
							Object.entries(feature).map(([key, value], entryIndex) => (
								<tr key={`${index}-${entryIndex}`}>
									<td>{key}</td>
									<td>
										{Array.isArray(value)
											? value.map((v, idx) => (
												<React.Fragment key={idx}>
													{v}
													<br />
												</React.Fragment>
											))
										: value}
									</td>
									<td></td>
								</tr>
							))
						))}
					</tbody>
				</table>
			</Card.Body>
		</Card>
	)
}

export default WordAnalysis;
