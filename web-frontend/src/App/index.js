import React from 'react';
import styled from 'styled-components';

import { ApolloProvider } from '@apollo/react-hooks';
import { apolloClient } from 'utils/apollo';

import LightsControl from './LightsControl';

const Wrapper = styled.div`
  display: flex;
  flex-direction: column;
  align-items: left;
  margin: 0 auto;
  padding: 0 1em;
  max-width: 90vw;
`;

const App = () => {
  return (
    <ApolloProvider client={apolloClient}>
      <Wrapper>
        <LightsControl />
      </Wrapper>
    </ApolloProvider>
  );
};

export default App;
