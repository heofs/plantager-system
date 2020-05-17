import ApolloClient from 'apollo-boost';

const uri = process.env.REACT_APP_API_URL || 'http://localhost:4000/graphql';

export const apolloClient = new ApolloClient({ uri });
