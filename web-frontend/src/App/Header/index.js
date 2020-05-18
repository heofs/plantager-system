import React, { useState } from 'react';
import styled from 'styled-components';
import { Input } from 'antd';

const Wrapper = styled.header`
  text-align: center;
  margin: 1em 0;
`;
const StyledInput = styled(Input)`
  width: 50%;
`;

export const Header = () => {
  const [isEditing, setEditing] = useState(false);
  const [text, setText] = useState('Your grow');

  return (
    <Wrapper onClick={() => setEditing(true)}>
      {isEditing ? (
        <StyledInput
          value={text}
          size="large"
          onBlur={() => setEditing(false)}
          onChange={(e) => setText(e.target.value)}
          onPressEnter={() => setEditing(false)}
        />
      ) : (
        <h1>{text}</h1>
      )}
    </Wrapper>
  );
};

export default Header;
