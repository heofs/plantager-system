import express from "express";
import { ApolloServer } from "apollo-server-express";

import resolvers from "./resolvers";
import typeDefs from "./type-defs";

const { SERVER_PORT = 4000 } = process.env;

const server = new ApolloServer({ resolvers, typeDefs });

const app = express();
server.applyMiddleware({ app });

app.listen({ port: SERVER_PORT }, () =>
  console.log(
    `🚀 Server ready at http://localhost:${SERVER_PORT}${server.graphqlPath}`
  )
);

app.get("/status", function(req, res) {
  res.send({ status: "OK" });
});
