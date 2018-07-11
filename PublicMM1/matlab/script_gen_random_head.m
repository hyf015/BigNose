%Generate a random head, render it and export it to PLY file
warning('off');
for i=1:11150
[model, msz] = load_model();
% Generate a random head
alpha = randn(msz.n_shape_dim, 1);
beta  = randn(msz.n_tex_dim, 1);
shape  = coef2object( alpha, model.shapeMU, model.shapePC, model.shapeEV );
tex    = coef2object( beta,  model.texMU,   model.texPC,   model.texEV );

% Render it
rp     = defrp;
%rp.phi = 0.5;
rp.phi = 0;
rp.dir_light.dir = [0;0;1];
rp.dir_light.intens = 0.6*ones(3,1);
ma = [rand(1,2)*0.6 + 0.35 rand*0.3 1];
lgt = rand(1,2)*160 - 80;
if i<10001
display_face(shape, tex, model.tl, rp, ma, lgt, sprintf('../../data/face/test/near/%05d',i));
display_face2(shape, tex, model.tl, rp, ma, lgt, sprintf('../../data/face/test/far/%05d',i));
else
display_face(shape, tex, model.tl, rp, ma, lgt, sprintf('../../data/face/train/near/%05d',i));
display_face2(shape, tex, model.tl, rp, ma, lgt, sprintf('../../data/face/train/far/%05d',i));
end
close all;
end

% Save it in PLY format
%plywrite('rnd_head.ply', shape, tex, model.tl );


% Generate versions with changed attributes
% apply_attributes(alpha, beta)
% 
% % Generate a random head with different coefficients for the 4 segments
% shape = coef2object( randn(msz.n_shape_dim, msz.n_seg), model.shapeMU, model.shapePC, model.shapeEV, model.segMM, model.segMB );
% tex   = coef2object( randn(msz.n_tex_dim,   msz.n_seg), model.texMU,   model.texPC,   model.texEV,   model.segMM, model.segMB );
% 
% plywrite('rnd_seg_head.ply', shape, tex, model.tl );
% display_face(shape, tex, model.tl, rp);
