import { gql } from "apollo-server-express";

export default gql`
  type Query {
    """
    Test Message.
    """
    person(id: ID!): Person!
    allPersons: [Person]!
  }

  type Person {
    id: ID!
    name: String
  }
`;
